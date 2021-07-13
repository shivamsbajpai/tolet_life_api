## Product Category Table

### Master Query

```sql
SELECT CONCAT('INSERT INTO public."ProductCategory"("product_category_id", "product_category") VALUES (',
'''',"product_category_id", '''', ', ' , '''', "product_category", '''', ' );')
FROM public."ProductCategory"
ORDER BY "product_category_id";
```

### Queries
```sql

INSERT INTO public."ProductCategory"("product_category_id", "product_category") VALUES ('4ab08c53-88dc-4c13-b6af-2e1e5b460b08', 'Property' );"
INSERT INTO public."ProductCategory"("product_category_id", "product_category") VALUES ('ac7d65f8-836c-4eba-9c51-664b97cf7d9f', 'Electronics' );"
INSERT INTO public."ProductCategory"("product_category_id", "product_category") VALUES ('aca4b6dd-106a-44a5-bb88-dd8c868097bd', 'Others' );"
INSERT INTO public."ProductCategory"("product_category_id", "product_category") VALUES ('c34b126f-a3ee-442c-a900-bd74f2e44f88', 'Furniture' );"
```

## Status Table

## Master Query

```sql
SELECT CONCAT('INSERT INTO public."Status"("status_id", "status") VALUES (',
'''',"status_id", '''', ', ' , '''', "status", '''', ' );')
FROM public."Status"
ORDER BY "status_id";
```

### Queries

```sql
INSERT INTO public."Status"("status_id", "status") VALUES ('3cb9559b-fe39-4e6b-9f58-25ed7c18003f', 'Active' );
```