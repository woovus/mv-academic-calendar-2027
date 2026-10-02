from datetime import date, timedelta as td
import hashlib
Y=2027
CATS={
 'term':('🟦','School Term','Term start/end & reporting days'),
 'break':('🟩','School Break','Term holidays & mid-breaks'),
 'exam':('🟥','Exam','Exams & assessments'),
 'public':('🟨','Public Holiday','Public holidays'),
 'other':('🟪','School Activity','PD days, transfers, admissions, camps'),
}
def d(m,dd,y=Y): return date(y,m,dd)
E=[ # cat,title,start,end(inclusive)
('term',"Teachers' Reporting Day 2027",d(1,13),d(1,13)),
('term',"Beginning of Academic Year 2027",d(1,17),d(1,17)),
('term',"Beginning of AL Batch 2027 (B-27)",d(1,31),d(1,31)),
('term',"End of First Term 2027",d(7,15),d(7,15)),
('term',"Beginning of Second Term 2027",d(8,1),d(8,1)),
('term',"End of Second Term 2027",d(12,9),d(12,9)),
('term',"Teachers' Reporting Day 2028",d(1,5,2028),d(1,5,2028)),
('term',"Beginning of Academic Year 2028",d(1,9,2028),d(1,9,2028)),
('break',"First Term Mid-Break",d(5,16),d(5,22)),
('break',"First Term Holidays",d(7,16),d(7,31)),
('break',"Second Term Mid-Break",d(9,19),d(9,25)),
('break',"Second Term Holidays",d(12,10),d(1,4,2028)),
('exam',"Gr. 11 Mock & Gr. 12 Term Exam",d(4,1),d(4,15)),
('exam',"First Term Exam",d(6,29),d(7,10)),
('exam',"Gr. 10 Mock Exam",d(8,26),d(9,9)),
('exam',"Gr. 11 (B-27) & Gr. 12 Mock Exam",d(8,26),d(9,9)),
('exam',"National Curriculum Assessment",d(10,31),d(11,10)),
('exam',"Second Term Exam",d(11,23),d(12,4)),
('other',"Professional Development",d(3,21),d(3,25)),
('other',"Professional Development",d(4,22),d(4,22)),
('other',"Professional Development",d(11,4),d(11,4)),
('other',"Children's Day (half-day teaching)",d(5,10),d(5,10)),
('other',"School Transfer Period 1",d(5,9),d(6,10)),
('other',"Camps and Activities (KS1-KS4)",d(6,12),d(6,14)),
('other',"New Admission - LKG & Gr. 1",d(7,4),d(8,31)),
('other',"Teachers' Day (half-day teaching)",d(10,5),d(10,5)),
('other',"School Transfer Period 2",d(10,10),d(11,9)),
('public',"New Year 2027",d(1,1),d(1,1)),
('public',"First of Ramadan",d(2,8),d(2,8)),
('public',"Last 10 Days of Ramadan",d(2,26),d(3,7)),
('public',"Eid-al-Fitr",d(3,9),d(3,9)),
('public',"Eid-al-Fitr Holiday",d(3,10),d(3,11)),
('public',"Labour Day",d(5,1),d(5,1)),
('public',"Hajj Day",d(5,16),d(5,16)),
('public',"Eid-al-Adha",d(5,17),d(5,17)),
('public',"Eid-al-Adha Holiday",d(5,18),d(5,20)),
('public',"Islamic New Year 1449",d(6,6),d(6,6)),
('public',"Independence Day",d(7,26),d(7,26)),
('public',"Independence Day Holiday",d(7,27),d(7,27)),
('public',"National Day",d(8,3),d(8,3)),
('public',"Prophet Muhammad's (SAW) Birthday",d(8,14),d(8,14)),
('public',"The Day Maldives Embraced Islam",d(9,3),d(9,3)),
('public',"Victory Day",d(11,3),d(11,3)),
('public',"Republic Day",d(11,11),d(11,11)),
('public',"New Year 2028",d(1,1,2028),d(1,1,2028)),
]
f=lambda x:x.strftime('%Y%m%d')
def build(name,items):
    L=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//Maldives Academic Calendar 2027//EN","CALSCALE:GREGORIAN",
       f"X-WR-CALNAME:{name}","X-WR-TIMEZONE:Indian/Maldives","X-WR-CALDESC:Source: Ministry of Education Maldives - Academic Calendar 2027 (TENTATIVE 1-Oct-26)"]
    for c,t,s,e in items:
        em,lab,_=CATS[c]
        uid=hashlib.md5((c+t+f(s)).encode()).hexdigest()+"@mv-academic-2027"
        L+=["BEGIN:VEVENT",f"UID:{uid}","DTSTAMP:20261001T000000Z",f"DTSTART;VALUE=DATE:{f(s)}",
            f"DTEND;VALUE=DATE:{f(e+td(1))}",f"SUMMARY:{em} {t}",f"CATEGORIES:{lab}",
            f"DESCRIPTION:{lab} - Tentative calendar (1 Oct 2026). Dates may change.","TRANSP:TRANSPARENT","END:VEVENT"]
    L.append("END:VCALENDAR")
    return "\r\n".join(L)+"\r\n"
open("calendar.ics","w",encoding="utf-8").write(build("Maldives Academic Calendar 2027",E))
for c,(em,lab,_) in CATS.items():
    open(f"{c}.ics","w",encoding="utf-8").write(build(f"{em} MV {lab} 2027",[x for x in E if x[0]==c]))
print(len(E))
