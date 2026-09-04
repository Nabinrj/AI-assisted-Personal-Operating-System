export type User={id:number;email:string;display_name:string};
export type Task={id:number;title:string;status:string;priority:number;completed:boolean;actual_minutes:number;estimated_minutes:number};
export type Goal={id:number;title:string;horizon:string;status:string;priority:number;success_metric:string};
export type Project={id:number;title:string;status:string;objective:string;next_action:string;blocker:string};
export type Skill={id:number;name:string;current_level:number;target_level:number};
export type TimeEntry={id:number;category:string;started_at:string;duration_minutes:number;note:string};
export type Income={id:number;source:string;amount:number;currency:string;received_at:string;note:string};
export type Research={id:number;question:string;hypothesis:string;experiment:string;result:string;conclusion:string;status:string};
