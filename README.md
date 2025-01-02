# mapGarbledArabicText
This is a Python script that may be useful if you have a lot of text containing Arabic characters which had originally been encoded using Windows 1256 (or cp1256) but was then stored as UTF8, resulting in you seeing garbled text like 'ãßÇä' instead of 'مكان' in your database.

# Purpose
I was working on migrating an old website to a new hosting server. The old site had a mariadb database containing mixed English and Arabic content. When moved to the new server, the Arabic characters would show as garbled text (for example ãßÇä) when viewing the database in phpMyAdmin, and a different set of (also garbled) text on the webpages. My solution was to map the garbled text characters to Arabic characters and then replace them in sql dump files which were then used to recreate the tables with the proper Arabic characters. The character sets of the newly recreated tables were set to UTF8 and collation to utf8mb4_unicode_ci.

# Step-by-step
0. MAKE SURE you are working with a backup of your database. DO NOT work on your live database or you could risk corrupting it.
1. Create two blank text files, name them input.sql and output.sql.
2. Make sure your table's character set is utf8, and that collation is utf8mb4_unicode_ci.
3. Export your table into an sql dump file.
4. Copy all the content of your sql dump file and paste it into input.sql.
5. Edit the script, ensuring you have the correct paths to input.sql and output.sql.
6. Run the script. This should populate output.sql with an SQL script that will recreate your table and insert the content with the corrected characters.
7. Rename your existing database table to indicate it is the original table (eg rename posts to post.OLD).
8. Take the newly generated contents of output.sql and execute them in phpMyAdmin (or whatever client you use to interact with your database). This should recreate your table inserting the correct Arabic characters.
9. Go back to step 3 and do steps 3-6 with your other tables.
