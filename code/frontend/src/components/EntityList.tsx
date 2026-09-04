import React from 'react';
export function EntityList({title,items,empty,onAdd}:{title:string;items:React.ReactNode[];empty:string;onAdd:()=>void}){return <section className="card list"><div className="row"><h2>{title}</h2><button className="primary" onClick={onAdd}>+ Add</button></div>{items.length?items:<p className="empty">{empty}</p>}</section>}
export function Metric({label,value}:{label:string;value:string|number}){return <div className="card metric"><span>{label}</span><strong>{value}</strong></div>}
