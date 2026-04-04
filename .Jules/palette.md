## 2024-05-24 - Semantic Range Input Outputs
**Learning:** For custom slider displays where the current value of an `<input type="range">` is shown visually in text next to it, using a plain `<span>` element means screen readers won't automatically associate the displayed value with the input.
**Action:** Use an `<output>` element instead of a `<span>` and add a `for="inputId"` attribute. This binds the displayed value properly to the input, ensuring screen readers can politely announce changes. Also ensure that `<canvas>` elements have `role="img"` and `aria-label="..."` attributes so they aren't ignored or read out awkwardly by screen readers.

## 2024-07-26 - Contrast on Bright Accents
**Learning:** Mid-tone brand colors (like the `#1abc9c` turquoise used for value displays) often fail WCAG AA contrast requirements when paired with white text. This makes small text difficult to read, especially for users with visual impairments.
**Action:** Establish a reusable pattern of using the dark background color (`#1a252f`) for text on bright accent backgrounds to ensure clear readability and pass contrast requirements.