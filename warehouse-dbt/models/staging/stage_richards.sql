with source_richards as (
  select * from {{ source('richards_sensors', 'richards_sensors')}}
),

final as (
  select * from source_richards
)

select * from final

