PGDMP     5                     {            TD_DataEngineer_Assignment    14.5    14.4     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16708    TD_DataEngineer_Assignment    DATABASE        CREATE DATABASE "TD_DataEngineer_Assignment" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.874';
 ,   DROP DATABASE "TD_DataEngineer_Assignment";
                postgres    false            ?            1259    16717    product_class_master    TABLE     ?   CREATE TABLE public.product_class_master (
    product_class_id integer NOT NULL,
    product_class_name character varying(100) NOT NULL
);
 (   DROP TABLE public.product_class_master;
       public         heap    postgres    false            ?            1259    16712    product_master    TABLE     ?   CREATE TABLE public.product_master (
    product_id integer NOT NULL,
    product_name character varying(100) NOT NULL,
    retail_price integer NOT NULL,
    product_class_id integer NOT NULL
);
 "   DROP TABLE public.product_master;
       public         heap    postgres    false            ?            1259    16709    sales_transaction    TABLE     ?   CREATE TABLE public.sales_transaction (
    transaction_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL
);
 %   DROP TABLE public.sales_transaction;
       public         heap    postgres    false            ?            1259    16747    sales_summary_report    VIEW     E  CREATE VIEW public.sales_summary_report AS
 SELECT sub_query.product_class_name,
    sub_query.rank,
    sub_query.product_name,
    sub_query.sales_value
   FROM ( SELECT product_class.product_class_name,
            row_number() OVER (PARTITION BY product_class.product_class_name ORDER BY (sum((sales.quantity * product.retail_price))) DESC, (sum(sales.quantity)) DESC) AS rank,
            product.product_name,
            sum((sales.quantity * product.retail_price)) AS sales_value
           FROM ((public.sales_transaction sales
             LEFT JOIN public.product_master product ON ((sales.product_id = product.product_id)))
             LEFT JOIN public.product_class_master product_class ON ((product.product_class_id = product_class.product_class_id)))
          GROUP BY product_class.product_class_name, product.product_name
          ORDER BY product_class.product_class_name, (row_number() OVER (PARTITION BY product_class.product_class_name ORDER BY (sum((sales.quantity * product.retail_price))) DESC, (sum(sales.quantity)) DESC))) sub_query
  WHERE (sub_query.rank <= 2);
 '   DROP VIEW public.sales_summary_report;
       public          postgres    false    210    210    211    210    210    209    209    211            ?          0    16717    product_class_master 
   TABLE DATA           T   COPY public.product_class_master (product_class_id, product_class_name) FROM stdin;
    public          postgres    false    211   ?       ?          0    16712    product_master 
   TABLE DATA           b   COPY public.product_master (product_id, product_name, retail_price, product_class_id) FROM stdin;
    public          postgres    false    210          ?          0    16709    sales_transaction 
   TABLE DATA           Q   COPY public.sales_transaction (transaction_id, product_id, quantity) FROM stdin;
    public          postgres    false    209   _       j           2606    16721 .   product_class_master product_class_master_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.product_class_master
    ADD CONSTRAINT product_class_master_pkey PRIMARY KEY (product_class_id);
 X   ALTER TABLE ONLY public.product_class_master DROP CONSTRAINT product_class_master_pkey;
       public            postgres    false    211            h           2606    16716 "   product_master product_master_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.product_master
    ADD CONSTRAINT product_master_pkey PRIMARY KEY (product_id);
 L   ALTER TABLE ONLY public.product_master DROP CONSTRAINT product_master_pkey;
       public            postgres    false    210            k           2606    16722    sales_transaction product    FK CONSTRAINT     ?   ALTER TABLE ONLY public.sales_transaction
    ADD CONSTRAINT product FOREIGN KEY (product_id) REFERENCES public.product_master(product_id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 C   ALTER TABLE ONLY public.sales_transaction DROP CONSTRAINT product;
       public          postgres    false    210    209    3176            l           2606    16727    product_master product_class    FK CONSTRAINT     ?   ALTER TABLE ONLY public.product_master
    ADD CONSTRAINT product_class FOREIGN KEY (product_class_id) REFERENCES public.product_class_master(product_class_id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 F   ALTER TABLE ONLY public.product_master DROP CONSTRAINT product_class;
       public          postgres    false    211    3178    210            ?       x?3?t?I,.Vp?2??????,g?=... ??      ?   I   x?̷?0 ??9?O9?????;T?|?`??N??op????IT%?"?d?&?
?PT?{???????<      ?   <   x????@???0????t?9??YN??d???.?lR?p̵i????W?#?4t?     