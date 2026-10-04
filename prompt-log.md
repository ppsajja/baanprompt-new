# prompt-log.md บันทึกการใช้ AI ของกลุ่ม <ชื่อกลุ่ม>

กติกา: เพิ่มต่อท้ายเท่านั้น ห้ามแก้หรือลบบันทึกเดิม
ทุกบันทึกมี: เลขที่ | วันที่ | เครื่องมือ | คำสั่ง | สิ่งที่ AI ถามหรือรายงาน | คำตอบหรือการตัดสินใจของทีม | สิ่งที่ AI เดา (ถ้ามี)
AI จะเพิ่มบันทึกให้เองเมื่อใช้คำสั่ง /clarify /plan /tasks /implement ทีมเพิ่มเองได้เมื่อสั่งแก้นอกคำสั่ง

## #1 | <วันที่> | <เครื่องมือ> | <คำสั่ง>

## #2 | 2569-10-04 | Chat + filesystem | /tasks specs/002-booking/spec.md | สร้าง tasks.md จาก spec/plan ของ feature booking และตรวจว่าทุก AC มี task ที่ครอบคลุม พร้อมแยก task ที่รอ Open Questions | ทีมยืนยันใช้ spec/plan นี้เป็นแหล่งความจริง และยอมรับการใช้คำตอบที่เดาได้จาก Q-14, Q-18, Q-19, Q-22 เป็นค่าเบื้องต้นเพื่อให้ tasks สามารถวางลำดับได้ | AI เดา: Q-14 = ติดต่อ call center, Q-18 = 10 นาที, Q-19 = 30 วินาที, Q-22 = เก็บแต่ไม่ส่งออกนอกระบบ

## #3 | 2569-10-04 | Chat + filesystem | แก้ spec/plan/tasks ให้ใช้ stack ที่เลือกเอง | ปรับเอกสารให้ตรงกับข้อจำกัดที่ spec ระบุว่าไม่มีข้อจำกัดเชิง framework: Frontend React + Vite + Tailwind, Backend FastAPI, Database PostgreSQL | ทีมเลือก stack นี้เอง ไม่ใช่ข้อกำหนดจาก spec; สถานะเอกสารทั้งหมดปรับให้สอดคล้องกับ stack ใหม่

## #4 | 2569-10-04 | Bash + filesystem | /implement T-01 specs/002-booking/tasks.md | สร้าง monorepo scaffold สำหรับ booking: frontend React + Vite + Tailwind, backend FastAPI, PostgreSQL docker-compose, backend smoke tests | T-01 เสร็จแล้ว; frontend build ผ่านและ backend pytest ผ่าน (2 tests) โดยใช้ stack ตามที่เลือกเอง

