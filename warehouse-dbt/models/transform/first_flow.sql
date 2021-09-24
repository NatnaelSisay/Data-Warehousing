with first_flow as (
  select * from {{ ref('stage_richards')}}
),

final as (
  select
    flow1
    occupancy1
  from first_flow
)

select * from final