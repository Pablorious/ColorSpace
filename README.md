# Colorspace Utility

The Colorspace Utility is a Python tool designed to generate colors based on luminance and C-Lab or CIE-Lab standards, allowing for the creation of color palettes with similar perceived brightness. This utility, which depends on Pygame, is particularly useful for generating consistent color schemes in user interfaces or visual elements that adhere to brightness standards, such as those defined by IEEE.

## Features

- **Luminance-Based Color Generation**: Create colors with specific luminance ranges, ensuring consistent perceived brightness across different elements.
- **Random RGB Color Generation**: Generate random RGB values that fall within specified luminance thresholds, making it easier to maintain visual consistency.
- **C-Lab/CIE-Lab Standards**: Adheres to color standards for creating visually harmonious palettes.
- **Syntactic Sugar for Pygame**: Includes utility functions like `random_pos` for generating random positions on the canvas and `add_stars` for adding star-like elements to your screen.
- **Pygame Integration**: Designed to be used seamlessly with Pygame for developing visually appealing and brightness-consistent UIs.

## How to Use

1. **Run the Utility**:
   Start the program by running the Python script. The script opens a fullscreen window where you can interact with the visual elements.

   ```bash
   python colorspace.py
   ```

2. **Keyboard Controls**:
   - Press `W`: Add random stars to the screen with brightness variations.
   - Press `S`: Save the current screen as an image file (`starsurf.png`).
   - Press `C`: Clear the screen (reset to black).
   - Press `ESC`: Exit the program.

3. **Color Generation**:
   - The `random_color(l_min, l_max)` function generates random colors that fall within the specified luminance range, ensuring a consistent look and feel.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install the required dependencies:
   ```bash
   pip install pygame
   ```
2. Run the script:
   ```bash
   python colorspace.py
   ```

## Future Improvements

- Adding support for more advanced color manipulations, such as hue and saturation adjustments.
- Implementing additional color standards and metrics to further enhance palette generation.
