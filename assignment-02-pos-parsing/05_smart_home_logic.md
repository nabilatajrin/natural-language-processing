# Smart-home logic (sketch)

Example propositions:

- `MotionDetected`
- `DoorOpen`
- `AlarmOn`

Rules (implication):

- If motion and door open at night → turn alarm on
- If alarm on → notify owner

Predicate style: `At(time, location)`, `Detect(sensor, event)`.
