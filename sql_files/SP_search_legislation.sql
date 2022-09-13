CREATE PROCEDURE search_legislation
@search_text nvarchar(255)
AS

SELECT l.legislationversionid,
       l.title,
       p.content,
       ib.NAME [Issuing Body Name],
       j.NAME  [Jurisdiction Name]
FROM   legislations l
       JOIN leg_part_relationship lpr
         ON l.legislationsourceid = lpr.legislationsourceid
            AND l.legislationversionordinal = lpr.legislationversionordinal
       LEFT JOIN part p
              ON lpr.partsourceid = p.partsourceid
                 AND lpr.partversionordinal = p.partversionordinal
       LEFT JOIN issuing_body ib
              ON l.issuingbodysourceid = ib.sourceid
       LEFT JOIN jurisdiction j
              ON l.jurisdictionsourceid = j.sourceid
WHERE  l.title LIKE '%' + @search_text + '%'
        OR p.content LIKE '%' + @search_text + '%'
        OR ib.NAME LIKE '%' + @search_text + '%'
        OR j.NAME LIKE '%' + @search_text + '%' 

go


exec search_legislation @search_text = 'expectations'