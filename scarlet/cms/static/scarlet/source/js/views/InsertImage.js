'use strict'
import Insert from '../helpers/Insert'

const InsertImage = Insert.extend({

  bindInputs : function () {
    Insert.prototype.bindInputs.apply(this)
    this.$dom.find('[data-respond=\"true\"]').on("change", this.onInput.bind(this));
  },

  // Generates or updates the image with the latest input value.
  onInput : function (e) {
    console.log('thing', e)
		let $target = $(e.currentTarget)
		let attribute = $target.data('attribute')
		let value = $(e.currentTarget).val()
		let $preview = this.$dom.find(".image-preview")
		let $img = $preview.find('img')

  	// Adjusts the source to come from the data attribute.
  	if ($target.attr('data-src')) {
  		$preview.empty()
  		$img = $preview.find('img')
  		value = $target.attr('data-src')
  	}

  	if (!$img.length) {

      $img = $("<img />")
      $preview.append($img)

      this.vars.$node = $img

      $img.on("load", (e) => {

        let width = $img.width()
        let height = $img.height()

        this.vars.size.width = width
        this.vars.size.height = height

        this.setAttribute("width", width)
        this.setAttribute("height", height)

  		})

  	} else {
  		this.vars.$node = $img
  	}

  	if (attribute === "width" || attribute === "height") {

  		value = value.replace("px", "")

  		if (this.vars.constrain) {
  			this.constrainProportion(attribute, value)
  		}

  		this.vars.size[attribute] = value

  	}

  	this.vars.$node = $img.attr(attribute, value)

  }

})

export default InsertImage