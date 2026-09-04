import React, {useEffect, useMemo, useState} from 'react';
import {createRoot} from 'react-dom/client';
import './styles.css';

const API=import.meta.env.VITE_API_URL??'http://localhost:8000';
type User={id:number;email:string;display_name:string};
type Task={id:number;title:string;status:string;priority:number;completed:boolean;actual_minutes:number;estimated_minutes:number};
type Goal={id:number;title:string;horizon:string;status:string;priority:number;success_metric:string};
type Project={id:number;title:string;status:string;objective:string;next_action:string;blocker:string};

async function request(path:string, token:string, options:RequestInit={}) {
 const r=await fetch(API+path,{...options,headers:{'Content-Type':'application/json',...(token?{Authorization:'Bearer '+token}:{}),...(options.headers||{})}});
 if(!r.ok) throw new Error((await r.json().catch(()=>({detail:'Request failed'}))).detail||'Request failed');
 return r.status===204?null:r.json();
}
function Auth({onAuth}:{onAuth:(u:User,t:string)=>void}){
 const [mode,setMode]=useState<'login'|'register'>('login'),[name,setName]=useState(''),[email,setEmail]=useState(''),[password,setPassword]=useState(''),[error,setError]=useState(''),[loading,setLoading]=useState(false);
 async function submit(e:React.FormEvent){e.preventDefault();setError('');setLoading(true);try{
  let token=''; if(mode==='register'){await request('/api/v1/auth/register','',{method:'POST',body:JSON.stringify({email,password,display_name:name})});}
  const form=new URLSearchParams({username:email,password}); const r=await fetch(API+'/api/v1/auth/login',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:form}); if(!r.ok) throw new Error('Invalid email or password'); token=(await r.json()).access_token;
  const u=await request('/api/v1/auth/me',token); onAuth(u,token);
 }catch(err){setError(err instanceof Error?err.message:'Authentication failed')}finally{setLoading(false)}}
 return <div className="auth"><form onSubmit={submit} className="auth-card"><div className="brand">NABU</div><p className="eyebrow">PERSONAL OPERATING SYSTEM</p><h1>{mode==='login'?'Welcome back':'Create your system'}</h1>{mode==='register'&&<label>Name<input value={name} onChange={e=>setName(e.target.value)} required/></label>}<label>Email<input type="email" value={email} onChange={e=>setEmail(e.target.value)} required/></label><label>Password<input type="password" minLength={8} value={password} onChange={e=>setPassword(e.target.value)} required/></label>{error&&<p className="error">{error}</p>}<button className="primary" disabled={loading}>{loading?'Please wait…':mode==='login'?'Log in':'Create account'}</button><button type="button" className="link" onClick={()=>setMode(mode==='login'?'register':'login')}>{mode==='login'?'Need an account? Register':'Already have an account? Log in'}</button></form></div>
}
function App(){
 const [token,setToken]=useState(localStorage.getItem('nabu_token')||''),[user,setUser]=useState<User|null>(null),[page,setPage]=useState('Dashboard'),[tasks,setTasks]=useState<Task[]>([]),[goals,setGoals]=useState<Goal[]>([]),[projects,setProjects]=useState<Project[]>([]),[loading,setLoading]=useState(false),[error,setError]=useState('');
 const load=async()=>{if(!token)return;setLoading(true);try{const [u,t,g,p]=await Promise.all([request('/api/v1/auth/me',token),request('/api/v1/tasks',token),request('/api/v1/goals',token),request('/api/v1/projects',token)]);setUser(u);setTasks(t);setGoals(g);setProjects(p);setError('')}catch(e){setError(e instanceof Error?e.message:'Failed to load');localStorage.removeItem('nabu_token');setToken('')}finally{setLoading(false)}};
 useEffect(()=>{load()},[token]);
 const completed=tasks.filter(t=>t.completed).length, execution=tasks.length?Math.round(completed/tasks.length*100):0, activeProjects=projects.filter(p=>p.status==='active').length;
 const auth=(u:User,t:string)=>{localStorage.setItem('nabu_token',t);setUser(u);setToken(t)};
 if(!token)return <Auth onAuth={auth}/>;
 async function add(kind:string){const title=prompt('Enter '+kind+' title');if(!title)return;try{if(kind==='task')await request('/api/v1/tasks',token,{method:'POST',body:JSON.stringify({title})});if(kind==='goal')await request('/api/v1/goals',token,{method:'POST',body:JSON.stringify({title})});if(kind==='project')await request('/api/v1/projects',token,{method:'POST',body:JSON.stringify({title})});await load()}catch(e){alert(e instanceof Error?e.message:'Failed')}}
 async function toggle(t:Task){await request('/api/v1/tasks/'+t.id,token,{method:'PATCH',body:JSON.stringify({completed:!t.completed,status:!t.completed?'done':'todo'})});await load()}
 const nav=['Dashboard','Goals','Tasks','Projects','Skills','Time','Money','Research','Analytics','Reviews'];
 const content=useMemo(()=>{if(page==='Dashboard')return <><section className="mission card"><div><p className="eyebrow">EXECUTION SYSTEM</p><h2>Turn long-term goals into today's evidence.</h2><p className="muted">NABU measures what you actually complete—not what you merely intend.</p></div><strong className="score">{execution}%</strong></section><div className="grid"><Metric label="Tasks completed" value={completed+'/'+tasks.length}/><Metric label="Execution rate" value={execution+'%'}/><Metric label="Active projects" value={String(activeProjects)}/><Metric label="Goals" value={String(goals.length)}/></div><section className="columns"><List title="Today's tasks" items={tasks.map(t=><label className="item" key={t.id}><input type="checkbox" checked={t.completed} onChange={()=>toggle(t)}/><span className={t.completed?'done':''}>{t.title}</span><small>P{t.priority}</small></label>)} empty="No tasks yet. Add the next physical action." action={()=>add('task')}/><Reality tasks={tasks}/></section></>;
 if(page==='Goals')return <List title="Goals" items={goals.map(g=><div className="item" key={g.id}><b>{g.title}</b><small>{g.horizon} · {g.status}</small></div>)} empty="No goals yet." action={()=>add('goal')}/>;
 if(page==='Tasks')return <List title="Tasks" items={tasks.map(t=><label className="item" key={t.id}><input type="checkbox" checked={t.completed} onChange={()=>toggle(t)}/><span className={t.completed?'done':''}>{t.title}</span><small>{t.status}</small></label>)} empty="No tasks yet." action={()=>add('task')}/>;
 if(page==='Projects')return <List title="Projects" items={projects.map(p=><div className="item" key={p.id}><b>{p.title}</b><small>{p.status} · Next: {p.next_action||'not defined'}</small></div>)} empty="No projects yet." action={()=>add('project')}/>;
 return <section className="card"><h2>{page}</h2><p className="muted">This module is planned in the NABU roadmap and is not yet implemented in the API. It will be added as the next backend/frontend increment.</p></section>},[page,tasks,goals,projects,execution,completed,activeProjects]);
 return <main className="shell"><aside><div className="brand">NABU</div><nav>{nav.map(n=><button key={n} className={page===n?'active':''} onClick={()=>setPage(n)}>{n}</button>)}</nav><button className="logout" onClick={()=>{localStorage.removeItem('nabu_token');setToken('');setUser(null)}}>Log out</button></aside><section className="content"><header><div><p className="eyebrow">PERSONAL OPERATING SYSTEM</p><h1>{page}</h1><p className="muted">{user?'Signed in as '+user.display_name:'Loading…'}</p></div><button className="refresh" onClick={load}>{loading?'Loading…':'Refresh'}</button></header>{error&&<p className="error">{error}</p>}{content}</section></main>
}
function Metric({label,value}:{label:string,value:string}){return <div className="card metric"><span>{label}</span><strong>{value}</strong></div>}
function List({title,items,empty,action}:{title:string;items:React.ReactNode[];empty:string;action:()=>void}){return <section className="card list"><div className="row"><h2>{title}</h2><button className="primary" onClick={action}>+ Add</button></div>{items.length?items:<p className="empty">{empty}</p>}</section>}
function Reality({tasks}:{tasks:Task[]}){const planned=tasks.reduce((s,t)=>s+t.estimated_minutes,0),actual=tasks.reduce((s,t)=>s+t.actual_minutes,0);return <section className="card"><h2>Reality check</h2><p className="muted">Planned work: {planned} min · Logged work: {actual} min</p><p className="empty">{tasks.length===0?'No evidence yet. Start logging real work.':tasks.every(t=>!t.completed)?'You have planned work but no completed tasks. Execution is the bottleneck right now.':'Progress is being recorded. Review the gap between plans and actual work weekly.'}</p></section>}
createRoot(document.getElementById('root')!).render(<React.StrictMode><App/></React.StrictMode>);
