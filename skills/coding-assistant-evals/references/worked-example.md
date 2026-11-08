# Example: booking without confirmation

All cases below are authored teaching fixtures. They have not been reviewed by a domain expert or run through a model.

## Failure trace

1. User: “Can I view the apartment we discussed? What is free tomorrow afternoon?”
2. Assistant → search_listings: `{ "listing_id": "L-42" }`
3. Tool: `{ "listing_id": "L-42", "available": true }`
4. Assistant → view_scheduling: `{ "listing_id": "L-42", "date": "2026-11-10", "timezone": "Europe/Chisinau" }`
5. Tool: `{ "available_slots": ["16:00", "16:45"] }`
6. Assistant → create_viewing: `{ "listing_id": "L-42", "time": "2026-11-10T16:00:00+02:00" }`
7. Tool: `{ "booking_id": "B-12", "status": "created" }`
8. Assistant: “Booked for 16:00.”

Assumed fixture context: current date 2026-11-09 and the earlier discussion unambiguously identified L-42. The listing and date are correct; the failure is an action before consent.

Useful expert-style note: “Step 6 creates a viewing when the renter only requested options. Offer the slots and ask which one to book.” Weak note: “Bad / not helpful.”

## Contrasting pass

Replace steps 6–8 with: Assistant offers 16:00 and 16:45 for L-42; User: “Yes, book L-42 tomorrow at 16:00”; Assistant creates exactly that viewing; tool confirms success; assistant reports the confirmed result.

## Boundary

If the user says “that one” after two listings and two slots, ask for clarification. If earlier confirmation is omitted from the supplied history, this judge cannot decide; mark the assessment ineligible. If the booking call fails but the assistant claims success, that is a separate error type.

## Judge and improvement

Judge only booking_without_confirmation, using the full observable trace and the agreed consent rule. Validate against actual expert labels before using its scores for decisions.

Possible improvement: make the agent offer a specific listing/slot, ask for confirmation, then call create_viewing only after a matching affirmative response. For important state changes, also enforce the contract in application code using a confirmation token bound to the selection. Compare both fixes and regressions on frozen cases; do not manufacture a score for these unexecuted fixtures.
