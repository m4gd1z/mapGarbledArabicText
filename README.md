# mapGarbledArabicText
This is a Python script that may be useful if you have a lot of text containing Arabic characters which had originally been encoded using Windows 1256 (or cp1256) but was then stored as UTF8, resulting in you seeing garbled text like 'ãßÇä' instead of 'مكان' in your database.

# Purpose
I was working on migrating an old website to a new hosting server. The old site had a mariadb database containing mixed English and Arabic content. When moved to the new server, the Arabic characters would show as garbled text (for example ãßÇä) when viewing the database in phpMyAdmin, and a different set of (also garbled) text on the webpages. My solution was to map the garbled text characters to Arabic characters and then replace them in sql dump files which were then used to recreate the tables with the proper Arabic characters. The character sets of the newly recreated tables were set to UTF8 and collation to utf8mb4_unicode_ci.

# Step-by-step
0. MAKE SURE you are working with a backup of your database. DO NOT work on your live database or you could risk corrupting it.
1. Create two blank text files, name them input.sql and output.sql.
2. Export your tables into sql dump files
3. Copy all the content of one of your sql dump files and paste it into input.sql.
4. Run the script. This should populate output.sql with SQL that will insert content with the corrected characters.
5. Rename your original table to indicate it is the original table (eg rename posts to post.OLD).
6. Take the newly generated contents of output.sql and execute them in phpMyAdmin (or whatever client you are using to interact with your database). This should recreate your table, and now your table should show the correct Arabic characters.
7. Go back to step 3 and do steps 3-6 with your other tables.
