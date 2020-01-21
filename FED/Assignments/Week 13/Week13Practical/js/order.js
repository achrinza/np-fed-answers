"use strict";

const orderForm = document.querySelector(".order-form");
const itemInput = orderForm.querySelector("[name=item]");
const qtyInput = orderForm.querySelector("[name=quantity]");
const nameInput = orderForm.querySelector("[name=name]");
const collectionDateInput = orderForm.querySelector("[name=collection-date]");
const allInput = orderForm.querySelectorAll("input, select");
const preSubmitFeedback = orderForm.querySelector(".pre-submit-feedback");
const submitFeedback = orderForm.querySelector(".submit-feedback");

const sellables = [
    {
        name: "Black bean purses",
        price: 3.95,
    },
    {
        name: "Southwestern Napoleons",
        price: 7.95,
    },
    {
        name: "Coconut-Corn Chowder",
        price: 3.95,
    },
    {
        name: "Jerk Rotisserie Chicken",
        price: 12.95,
    },
    {
        name: "Thai Shrimp Kebabs",
        price: 12.95
    },
    {
        name: "Pasta Puttanesca",
        price: 12.95
    },
];

function initItemSelect(itemInput) {
    sellables.forEach(x => {
        itemInput.innerHTML += `<option>${x.name}</option>`;
    });
}

function initCollectionDate(collectionDateInput) {
    collectionDateInput.min = new Date().toISOString().split("T")[0];
    collectionDateInput.max = new Date(new Date().setMonth(new Date().getMonth() + 1)).toISOString().split("T")[0];
}

function formPreSubmit(
        preSubmitFeedback,
        collectionDate,
        item,
        qty,
    ) {
    preSubmitFeedback.innerHTML = `You ordered ${qty} ${item.name}. Price = $${item.price} x ${qty} = $${item.price * qty}`
        + `\nCollection date: ${collectionDate.toISOString().split("T")[0]}`;
}

function formSubmit(
        submitFeedback,
        userName,
    ) {
    submitFeedback.innerHTML = `Thank you for the order, ${userName}`;
}

function formReset(
    preSubmitFeedback,
    submitFeedback,
) {
    preSubmitFeedback.innerHTML = "";
    submitFeedback.innerHTML = "";
}

function initForm(itemInput, collectionDateInput) {
    initItemSelect(itemInput);
    initCollectionDate(collectionDateInput);
}

initForm(itemInput, collectionDateInput);

orderForm.addEventListener("submit", e => {
    formSubmit(submitFeedback, nameInput.value);
    e.preventDefault();
});

orderForm.addEventListener("reset", () => {
    formReset(preSubmitFeedback, submitFeedback);
});

allInput.forEach(x => x.addEventListener("change", () => {
    const itemInputSelected = itemInput.querySelector("option:checked");
    if (orderForm.checkValidity()) {
        formPreSubmit(
            preSubmitFeedback,
            new Date(collectionDateInput.value),
            sellables.find(x => x.name == itemInputSelected.value),
            qtyInput.value,
        );
    }
}));
