function main() {
    $('.overfit_people').hide();

    $('.overfit').on('click', function() {
        var text = $(this).text();
        $(this).text(
            text == 'Show less' ? 'Show more!' : 'Show less');

        $(this).next().slideToggle(400);

    });
}
$(document).ready(main);
