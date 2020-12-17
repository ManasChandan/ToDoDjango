// // // console.log("Java Script Testing") ; 
// // // console.log($) ; 
// $(document).ready(function(){
//     $('#addButton').click(function(){
//         var serilaizeddata = $('#addingForm').serialize() ; 
//         console.log(serilaizeddata) ; 
//         var posting = $.post('addTodo' , serilaizeddata) ; 
//         posting.done(function(data){
//             $('#taskList').append(
//                 '<div class="card col-sm-3 mt-2 mx-auto">' + 
//                 '<img src="{% static "todo/dmc.jpg" %}" class="card-img-top" alt="...">'+
//                 '<div class="card-body">'+
//                 '<h5 class="card-title">Work To Do</h5>'+
//                 '<p class="card-text">'+ data.task.newcontents +'</p>'+
//                 '<a href="deleteTodo/{{content.id}}" method="post" class="btn btn-outline-danger">Delete</a>'+
//                 '</div></div>'
//             )
//         }) 
//     })  
// }) ; 
$( "#addingForm" ).submit(function( event ) {
 
    // Stop form from submitting normally
    event.preventDefault();
   
    // Get some values from elements on the page:
    var $form = $( this ),
      term = $form.serialize(),
      url = $form.attr( "action" );
   
    // Send the data using post
    var posting = $.post( url, term );
   
    // Put the results in a div
    posting.done(function( data ) {
        $('#rowLists').append(
                            '<div class="card col-sm-3 mt-2 mx-auto">' + 
                            '<img src="static/todo/dmc.jpg" class="card-img-top" alt="...">'+
                            '<div class="card-body">'+
                            '<h5 class="card-title">Work To Do</h5>'+
                            '<p class="card-text">'+ data.task.newcontents +'</p>'+
                            '<a href="deleteTodo/{{content.id}}" method="post" class="btn btn-outline-danger">Delete</a>'+
                            '</div></div>'
                        )
    });
  });