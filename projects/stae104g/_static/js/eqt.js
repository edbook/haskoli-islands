function grade_fill_in_blank(eqtBlock) {
    /* Find answer */
    var inputField = eqtBlock.find('.eqt-fib-answer input[name=answer]');
    var answeredValue = inputField.val();

    // Empty answer prompts no action
    if (answeredValue == "") {
        return null;
    }

    // Answer is correct
    if (answeredValue == inputField.data('answer')) {
        return true;
    }

    // Answer is incorrect
    return false;
}


function grade_multiple(eqtBlock) {
    // Get all the answer elements
    answers = eqtBlock.find('form > ol.eqt-answer-list > li input');
    var isCorrect = true;

    /* Loop over input element of each answer */
    answers.each(function() {
        if (($(this).prop('checked') && $(this).val() == "I") ||
            (!$(this).prop('checked') && $(this).val() == "C")) {
            // Answer is incorrect
            isCorrect = false;
            return;
        }
    });
    // Answer is correct
    return isCorrect
}


function grade_regular(eqtBlock) {
    answer_input = eqtBlock.find('form > ol.eqt-answer-list > li input:checked');
    // If none is clicked, return -1
    if (answer_input.length == 0) {
        return null;
    }
    // Return the answer
    if (answer_input.val() == "C") {
        return true;
    }
    return false;
}


function grade() {
    // Get the div element to process from above
    var eqtBlock = $(this).parent().parent();

    mode = eqtBlock.data('mode');
    if (mode == 'fill-in-blank') {
        answer = grade_fill_in_blank(eqtBlock);
    } else if (mode == 'multiple'){
        answer = grade_multiple(eqtBlock);
    } else {
        answer = grade_regular(eqtBlock);
    }

    // Grade button pushed with no answer given. Finish
    if (answer === null) {
        return;
    }

    /* Update element visibility
     * Show checked field explanations
     */
    if (answer === true) {
        eqtBlock.addClass('success');
        eqtBlock.find(".eqt-block-actions .result-icon").text("Correct !");
        evaluate_labels(eqtBlock, false);
    } else {
        eqtBlock.addClass('errored');
        eqtBlock.find('.eqt-block-actions .result-icon').text("Incorrect !");
        evaluate_labels(eqtBlock, true);
    }
    eqtBlock.find('form > ol.eqt-answer-list > li input:checked').parent().find('.tip.expl').show();

    // Disable inputs
    eqtBlock.find('form input').prop('disabled', true);
}


function again() {
    // Get the div element to process from above
    var eqtBlock = $(this).parent().parent();

    // Clean all the form fields
    eqtBlock.find('ol.eqt-answer-list > li > label').removeClass('correct incorrect');
    eqtBlock.find("form input").attr('checked', false);
    eqtBlock.find("form input[type='text']").val('');

    // Enable inputs
    eqtBlock.find('form input').prop('disabled', false);

    // Update element visibility
    eqtBlock.removeClass('success errored solution');
    eqtBlock.find(".tip.expl").hide();
}


function solution_fill_in_blank(eqtBlock) {
    var inputField = eqtBlock.find('.eqt-fib-answer input[name=answer]');
    inputField.val(inputField.data('answer'));
    eqtBlock.find(".tip.expl").show();
}


function solution_regular(eqtBlock) {
    eqtBlock.find(".tip.expl").show();
    evaluate_labels(eqtBlock, false);
}


function solution() {
    // Get the div element to process from above
    var eqtBlock = $(this).parent().parent();

    mode = eqtBlock.data('mode');
    if (mode == 'fill-in-blank') {
        solution_fill_in_blank(eqtBlock);
    } else {
        solution_regular(eqtBlock);
    }

    eqtBlock.removeClass('errored');
    eqtBlock.addClass('success solution');
}


function evaluate_labels(eqtBlock, onlySelected) {
    var selector = 'form > ol.eqt-answer-list > li input';
    if (onlySelected === true) {
        selector += ':checked'
    }
    eqtBlock.find(selector).each(function(){
        if ($(this).val() == "C") {
            $(this).parent().addClass('correct');
        } else {
            $(this).parent().addClass('incorrect');
        }
    })
}


$(function() {
    $('.eqt-block .eqt-actions.eqt-grade').on('click', grade);
    $('.eqt-block .eqt-actions.eqt-again').on('click', again);
    $('.eqt-block .eqt-actions.eqt-solution').on('click', solution);
});