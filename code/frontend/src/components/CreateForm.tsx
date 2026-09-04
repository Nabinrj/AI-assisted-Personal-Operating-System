import React,{useState} from 'react';
export function CreateForm({fields,onSubmit,onCancel}:{fields:{name:string;label:string;type?:string;required?:boolean}[];onSubmit:(data:Record<string,string>)=>Promise<void>;onCancel:()=>void}){
 const [data,setData]=useState<Record<string,string>>({}); const [busy,setBusy]=useState(false); const [error,setError]=useState('');
 async function submit(e:React.FormEvent){e.preventDefault();setBusy(true);setError('');try{await onSubmit(data)}catch(x){setError(x instanceof Error?x.message:'Could not save')}finally{setBusy(false)}}
 return <form className="card form" onSubmit={submit}>{fields.map(f=><label key={f.name}>{f.label}<input type={f.type||'text'} required={f.required} value={data[f.name]||''} onChange={e=>setData({...data,[f.name]:e.target.value})}/></label>)}{error&&<p className="error">{error}</p>}<div className="row"><button type="button" className="refresh" onClick={onCancel}>Cancel</button><button className="primary" disabled={busy}>{busy?'Saving…':'Save'}</button></div></form>
}
