select postalcode as ZIPCODE, fileddate as FileDate, count(postalcode) as TotalEviction 
from oca_addresses as A
inner join oca_index as I 
on A.indexnumberId = I.indexnumberId 
where city = 'New York'
	and classification = any('{Holdover,Non-Payment}') 
group by postalcode, fileddate
