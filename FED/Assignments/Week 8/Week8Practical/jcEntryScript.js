const jcCutoffPoints = {
    ACJC: 8,
    AJC: 11,
    CJC: 10,
    EJC: 9,
    HCI: 4,
    NJC: 7,
    NYJC: 7,
    SAJC: 10,
    TJC: 9,
    VJC: 7
}

const jcSelector = document.querySelector('.block-jc-cutoffs__selector');
const jcCutoffResults = document.querySelector('.block-jc-cutoffs__results');

const updateCutoffResults = (jcCutoffPoints, jcSelector, jcCutoffResults) => {
    switch (jcSelector.value) {
        case 'Select a JC':
            jcCutoffResults.innerHTML = 'Select a JC';
            break;
        default:
            jcCutoffResults.innerHTML = `Entry Point for ${jcSelector.value} is ${jcCutoffPoints[jcSelector.value]}`;
    }
}

jcSelector.innerHTML += '<option>Select a JC</option>';

Object.keys(jcCutoffPoints).forEach(x => {
    jcSelector.innerHTML += `<option>${x}</option>`;
});

jcSelector.addEventListener('input', () => updateCutoffResults(jcCutoffPoints, jcSelector, jcCutoffResults));

updateCutoffResults(jcCutoffPoints, jcSelector, jcCutoffResults);
