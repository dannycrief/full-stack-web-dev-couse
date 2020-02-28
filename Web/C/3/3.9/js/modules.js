function jQuery(selector, context = document) {
    this.elements = Array.from(context.querySelectorAll(selector));
    return this
}

jQuery.prototype.each = function (fn) {
    this.elements.forEach((element, index) => fn.call(element, element, index));
    return this;
};

jQuery.prototype.click = function (fn) {
    this.each(element => element.addEventListener('click', fn));
    return this;
};

jQuery.prototype.hide = function () {
    this.each(element => element.style.display = 'none');
    return this;
};

jQuery.prototype.show = function () {
    this.each(element => element.style.display = '');
    return this;
};

jQuery.prototype.remove = function () {
    this.each(element => element.remove());
    return this;
};

jQuery.prototype.class = function (name) {
    this.each(element => element.className = name);
    return this;
};

jQuery.prototype.html = function (text) {
    this.each(element => element.innerHTML = text);
    return this;
};

jQuery.prototype.text = function (text) {
    this.each(element => element.innerText = text);
    return this;
};

jQuery.prototype.getElementAttribute = function(elementName) {
    this.each(element => element.getAttribute(elementName));
    return this;
}

jQuery.prototype.setElementAttribute = function(elementName, elementValue) {
    this.each(element => element.setAttribute(elementName, elementValue));
    return this;
}

jQuery.prototype.removeElementAttribute = function(elementName) {
    this.each(element => element.removeAttribute(elementName));
    return this;
}


const $ = (e) => new jQuery(e);