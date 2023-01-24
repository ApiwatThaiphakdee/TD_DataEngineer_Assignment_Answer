CREATE OR REPLACE VIEW sales_summary_report AS
SELECT * FROM
(
SELECT product_class.product_class_name,
	   ROW_NUMBER() OVER(PARTITION BY product_class_name ORDER BY SUM(sales.quantity * product.retail_price) DESC,SUM(sales.quantity) DESC) AS rank,
       product.product_name,
       SUM(sales.quantity * product.retail_price) AS sales_value
FROM sales_transaction AS sales
LEFT JOIN product_master AS product ON sales.product_id = product.product_id
LEFT JOIN product_class_master AS product_class ON product.product_class_id = product_class.product_class_id
GROUP BY product_class.product_class_name,product.product_name
ORDER BY product_class.product_class_name ASC,rank ASC
) 
AS sub_query
WHERE rank <= 2;