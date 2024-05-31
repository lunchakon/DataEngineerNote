## Querying JSON Data in PostgreSQL

### Example Json Data structure
    [{"dataset": "JP_INTERNAL", "records": ["JP_CONTRIB/DEPO/?*", "JP_CONTRIB/FX/?*"]}, {"dataset": "HK_INTERNAL", "records": ["AU_CONTRIB/FX/?*", "CN_CONTRIB/FX/?*", "HK_CONTRIB/DEPO/?*", "HK_CONTRIB/FX/?*", "HK_CONTRIB/IRS/?*", "KR_CONTRIB/NDF/?*", "REF/FX/?*", "SG_CONTRIB/BILL/?*", "SG_CONTRIB/BOND/?*", "SG_CONTRIB/FRN/?*", "SG_CONTRIB/FX/?*", "SG_CONTRIB/NDF/?*", "SG_INTERNAL/NDF/?*"]}]

To find rows where any part of the JSON data contains "SG_INTERNAL", you can use the jsonb type and the @> operator or the jsonb_array_elements function to extract and search through the JSON array elements.


1.) Use the @> Operator: This operator checks if the JSONB data on the left contains the JSONB data on the right. This method checks for the presence of "SG_INTERNAL" in any dataset.

      SELECT *
      FROM tc.hub_service_instance hsi
      JOIN tc.hub_client_service hcs ON hsi.hub_client_service_id = hcs.hub_client_service_id
      WHERE hsi.read_permissions::jsonb @> '[{"dataset": "SG_INTERNAL"}]'::jsonb

2.) Use jsonb_array_elements to search through arrays: If the JSON structure is more complex and you need to search through nested arrays and objects.

    SELECT *
    FROM tc.hub_service_instance hsi
    JOIN tc.hub_client_service hcs ON hsi.hub_client_service_id = hcs.hub_client_service_id
    WHERE EXISTS (
        SELECT 1
        FROM jsonb_array_elements(hsi.read_permissions::jsonb) elem
        WHERE elem->>'dataset' LIKE '%SG_INTERNAL%'
           OR EXISTS (
               SELECT 1
               FROM jsonb_array_elements(elem->'records') rec
               WHERE rec::text LIKE '%SG_INTERNAL%'
           )
    )
