from ehrql import codelist_from_csv, show
from ehrql.tables.core import patients, practice_registrations, clinical_events, medications

index_date = "2024-03-31"

diabetes_codes = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-dm_cod.csv", column="code")
resolved_codes = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-dmres_cod.csv", column="code")

last_diagnosis_date = (
    clinical_events.where(clinical_events.snomedct_code.is_in(diabetes_codes))
    .sort_by(clinical_events.date)
    .where(clinical_events.date <= index_date)
    .last_for_patient()
    .date
)
last_resolved_date = (
    clinical_events.where(clinical_events.snomedct_code.is_in(resolved_codes))
    .sort_by(clinical_events.date)
    .where(clinical_events.date <= index_date)
    .last_for_patient()
    .date
)

has_unresolved_diabetes = last_diagnosis_date.is_not_null() & (
    last_resolved_date.is_null() | (last_resolved_date < last_diagnosis_date)
)

show(last_diagnosis_date, last_resolved_date, has_unresolved_diabetes)