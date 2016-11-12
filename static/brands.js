$("#model-year").on("change", function(evt){
    if (this.value.length === 4){
        // maybe this is valid input?? Let's ask!
        var currentModelName = $("#model").val();
        var currentBrandName = $("#brand").val();
        var sendPost = window.confirm("Would you like to add the " + currentBrandName + " " + currentModelName + " " + this.value + " to the database?");
        alert("Sorry, not implemented yet.");
    }
});