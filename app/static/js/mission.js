$(document).ready(function () {
    $('.task-board-container .task').each(function() {
        var status = $(this).find(".status");
        $(this).find(".action-complete").click(function() {
            status.text("Completed");
            $(this).parents(".actions").remove();
        });
        $(this).find(".action-reject").click(function() {
            status.text("Rejected");
            $(this).parents(".actions").remove();
        });
        $(this).find(".action-accept").click(function() {
            status.text("Accepted");
            $(this).removeClass("action-accept").addClass("action-complete").text("Complete").siblings('.action-reject').remove();
        });
        $(this).find(".action-take").click(function() {
            $(this).remove();
        });
    });
});