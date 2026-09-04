from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field

class SkillCreate(BaseModel):
 name:str=Field(min_length=1,max_length=120);current_level:int=Field(default=1,ge=1,le=10);target_level:int=Field(default=5,ge=1,le=10)
class SkillOut(SkillCreate):
 model_config=ConfigDict(from_attributes=True);id:int;user_id:int
class SkillEvidenceCreate(BaseModel):
 description:str=Field(min_length=1);url:str=""
class SkillEvidenceOut(SkillEvidenceCreate):
 model_config=ConfigDict(from_attributes=True);id:int;skill_id:int;completed_at:datetime
class TimeEntryCreate(BaseModel):
 category:str=Field(min_length=1,max_length=60);started_at:datetime;duration_minutes:int=Field(ge=1);note:str=""
class TimeEntryUpdate(BaseModel):
 category:str|None=None;duration_minutes:int|None=Field(default=None,ge=1);note:str|None=None
class TimeEntryOut(TimeEntryCreate):
 model_config=ConfigDict(from_attributes=True);id:int;user_id:int
class IncomeCreate(BaseModel):
 source:str=Field(min_length=1,max_length=120);amount:float=Field(gt=0);currency:str="NPR";received_at:datetime;note:str=""
class IncomeOut(IncomeCreate):
 model_config=ConfigDict(from_attributes=True);id:int;user_id:int
class DailyReviewCreate(BaseModel):
 review_date:date;completed_summary:str="";blocker:str="";tomorrow_priority:str=""
class DailyReviewOut(DailyReviewCreate):
 model_config=ConfigDict(from_attributes=True);id:int;user_id:int
class WeeklyReviewCreate(BaseModel):
 week_start:date;wins:str="";failures:str="";lessons:str="";next_week_priority:str=""
class WeeklyReviewOut(WeeklyReviewCreate):
 model_config=ConfigDict(from_attributes=True);id:int;user_id:int
class ResearchCreate(BaseModel):
 question:str=Field(min_length=1,max_length=500);hypothesis:str="";experiment:str="";result:str="";conclusion:str="";status:str="active"
class ResearchUpdate(BaseModel):
 hypothesis:str|None=None;experiment:str|None=None;result:str|None=None;conclusion:str|None=None;status:str|None=None
class ResearchOut(ResearchCreate):
 model_config=ConfigDict(from_attributes=True);id:int;user_id:int