# Inventory Enhancement Module - Odoo

## Overview

- The inventory_enhancement module is designed to enhance Odoo’s inventory management capabilities by adding features such as batch tracking, expiry date management, and automated stock adjustments.

## Features

-  Batch Tracking: Enables tracking of inventory batches for better traceability.
-  Expiry Date Management: Automatically manages product expiry dates and alerts users.
-  Automated Stock Adjustments: Adjusts stock levels based on predefined conditions.

## Direction for creation

Step 1:- first I created custom folder.
Step2:- then I created one module inventory_management.
Step3:- then i created _manifest.py and __init_.py file .
Step4:- after that I created model directory where I define _init_.py , product_template.py ,stock_location.py,stock_quant.py.
        _init_.py:- i import all models
        Product_template.py:- here I inherited product.template and define two field(batch number and expiry_date)
        Stock_location.py:- here I inherited stock.location and define one field(auto_adjust_stock)
        Stock_quant.py:- here I inherited stock.quant and define one function which adjust the stock 

Step5:- I created views directory and define all views by using inherit_id and xpath.
Step6:- i created data directory and there I define scheduler that will run every day based on function define on stock_quant.py and also define adjust stock for expiry scheduler.
Step7:- created one report and directly and define product_expiry_report.xml.
Step8:- created one security directory in which I define ir.model.access.csv in this I define access.
  
