CREATE TABLE "supermarket" (
    "id"  SERIAL  NOT NULL,
    "invoice_id" VARCHAR(80)   NOT NULL,
    "branch" VARCHAR(10)   NOT NULL,
    "city" VARCHAR(80)   NOT NULL,
    "customer_type" VARCHAR(80)   NOT NULL,
    "gender" VARCHAR(80)   NOT NULL,
    "product_line" VARCHAR(100)   NOT NULL,
    "unit_price" NUMERIC   NOT NULL,
    "quantity" INT   NOT NULL,
    "tax_5_percent" NUMERIC   NOT NULL,
    "total" NUMERIC   NOT NULL,
    "date" VARCHAR(40)   NOT NULL,
    "time" VARCHAR(40)   NOT NULL,
    "payment" VARCHAR(80)   NOT NULL,
    "cogs" NUMERIC   NOT NULL,
    "gross_margin_percent" NUMERIC NOT NULL,
    "gross_income" NUMERIC NOT NOT,
    "rating" NUMERIC NOT NULL,
    CONSTRAINT "pk_cms" PRIMARY KEY (
        "id"
     )
);