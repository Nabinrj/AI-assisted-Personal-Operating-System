import React from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

function App() {
  const [health, setHealth] = React.useState('checking');
  React.useEffect(() => {
    fetch(`${API}/health`).then(r => r.ok ? r.json() : Promise.reject()).then(() => setHealth('online')).catch(() => setHealth('offline'));
  }, []);
  return <main className="shell">
    <aside><div className="brand">NABU</div><nav>{['Dashboard','Goals','Tasks','Projects','Skills','Time','Money','Research','Analytics','Reviews'].map((x,i)=><button className={i===0?'active':''} key={x}>{x}</button>)}</nav></aside>
    <section className="content">
      <header><div><p className="eyebrow">PERSONAL OPERATING SYSTEM</p><h1>Command Center</h1><p className="muted">Turn your long-term goals into today's execution.</p></div><span className={`status ${health}`}>● API {health}</span></header>
      <div className="mission card"><div><p className="eyebrow">90-DAY MISSION</p><h2>Build and launch your first AI product</h2><p className="muted">Connect daily execution to a measurable outcome.</p></div><div className="progress"><strong>0%</strong><div><span style={{width:'0%'}}/></div></div></div>
      <div className="grid">{[['Deep work','0h','6h target'],['Learning','0h','2h target'],['Building','0h','3h target'],['Execution','0%','weekly']].map(([a,b,c])=><div className="card metric" key={a}><span>{a}</span><strong>{b}</strong><small>{c}</small></div>)}</div>
      <div className="columns"><div className="card"><div className="row"><h3>Today's actions</h3><button className="primary">+ Add task</button></div><p className="empty">No tasks yet. Create the first action that moves your 90-day mission forward.</p></div><div className="card"><h3>Reality check</h3><p className="empty">Reality checks will appear once NABU has execution data.</p></div></div>
    </section>
  </main>
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><App /></React.StrictMode>);
