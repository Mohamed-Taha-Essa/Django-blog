maing -->project

app--> posts

Db in Models:
-Post 
    -content
    -name_author
    -image
    -tag
    -draft
    -date_of_publish
    -category -->one to many

Comment :
    -content
    _name_user
    -date_time
    -Post

Category:
    -name


View :
    -post_list --> shwo all posts
    -post_detail --> deatail for post
    -creat_post --->
    -edit_post -->
    -delete_post 
    -update _post

Template :
    -post_list.html
    -post_dtail.html
    -post_edit.html
    -post_creat
    -post_update
    -post_delete