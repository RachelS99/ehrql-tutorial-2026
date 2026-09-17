from ehrql import show
from ehrql.tables.core import patients, practice_registrations, clinical_events, medications

index_date = "2024-03-31"

# aged_17_or_older = patients.age_on(index_date) >= 17
# is_alive = patients.is_alive_on(index_date)

# show(
#     aged_17_or_older,
#     is_alive,
#     aged_17_or_older | is_alive)

# aged_17_or_older = (index_date - patients.date_of_birth).years >= 17
# is_alive = patients.date_of_death.is_null() | (patients.date_of_death > index_date)

# show(
#     aged_17_or_older,
#     is_alive,
#     aged_17_or_older & is_alive
# )

# show(
#     practice_registrations.start_date,
#     practice_registrations.start_date <= index_date
#     )

# show(practice_registrations.where(practice_registrations.start_date <= index_date))

# show(
#     practice_registrations
#     .where(practice_registrations.start_date <= index_date)
#     .except_where(practice_registrations.end_date <= index_date)
#     .exists_for_patient()
#     )

aged_17_or_older = patients.age_on(index_date) >= 17
is_alive = patients.is_alive_on(index_date)

is_registerd = (
    practice_registrations
    .where(practice_registrations.start_date <= index_date)
    .except_where(practice_registrations.end_date <= index_date)
    .exists_for_patient()
)

show(
    aged_17_or_older,
    is_alive,
    is_registerd,
    aged_17_or_older & is_alive & is_registerd
)