-- Write only the SQL statement that solves the problem and nothing else
select
  e.name ,
  case
    when e.mgrId is null
      then null
    else
      m.name
  end as manager
from employees e
  left join employees m
    on e.mgrId = m.id;
