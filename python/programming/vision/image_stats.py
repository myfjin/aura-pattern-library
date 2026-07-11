#!/usr/bin/env python3
"""
Histogram-based image contrast stretcher module.

This module provides functionality to enhance image contrast by stretching
the histogram of an image using percentile-based clipping and lookup table
(LUT) generation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Optional
import sys


class ImageStats:
    """
    Calculate and store image histogram statistics.
    
    This class computes histogram data and cumulative distribution
    for grayscale images represented as lists of pixel values.
    """
    
    def __init__(self, pixel_data: List[int], bit_depth: int = 8) -> None:
        """
        Initialize ImageStats with pixel data.
        
        Args:
            pixel_data: List of pixel intensity values (0-255 for 8-bit)
            bit_depth: Bit depth of the image (default 8 for 0-255 range)
            
        Raises:
            ValueError: If pixel data is empty or bit_depth is invalid
        """
        if not pixel_data:
            raise ValueError("Pixel data cannot be empty")
        if bit_depth <= 0:
            raise ValueError("Bit depth must be positive")
            
        self.pixel_data = pixel_data
        self.bit_depth = bit_depth
        self.max_value = (1 << bit_depth) - 1
        self.histogram = self._compute_histogram()
        self.cumulative_histogram = self._compute_cumulative_histogram()
        self.total_pixels = len(pixel_data)
        
    def _compute_histogram(self) -> List[int]:
        """Compute histogram of pixel intensities."""
        hist = [0] * (self.max_value + 1)
        for pixel in self.pixel_data:
            if 0 <= pixel <= self.max_value:
                hist[pixel] += 1
        return hist
    
    def _compute_cumulative_histogram(self) -> List[int]:
        """Compute cumulative histogram."""
        cum_hist = [0] * (self.max_value + 1)
        cum_sum = 0
        for i in range(len(self.histogram)):
            cum_sum += self.histogram[i]
            cum_hist[i] = cum_sum
        return cum_hist
    
    def get_percentile(self, percentile: float) -> int:
        """
        Get the intensity value at the specified percentile.
        
        Args:
            percentile: Percentile value (0.0 to 100.0)
            
        Returns:
            Intensity value at the specified percentile
            
        Raises:
            ValueError: If percentile is not between 0 and 100
        """
        if not 0 <= percentile <= 100:
            raise ValueError("Percentile must be between 0 and 100")
            
        # At least 1 pixel must be covered: percentile 0 means "the smallest
        # intensity present", not absolute 0 (cum_hist[0] >= 0 was trivially
        # true, so percentile 0 always answered 0 even for bright images).
        target_count = max((percentile / 100.0) * self.total_pixels, 1)
        for i in range(len(self.cumulative_histogram)):
            if self.cumulative_histogram[i] >= target_count:
                return i
        return self.max_value


class ContrastStretcher:
    """
    Stretch image contrast using histogram-based techniques.
    
    This class applies contrast stretching to images by computing
    a lookup table based on percentile clipping.
    """
    
    def __init__(self, min_percentile: float = 1.0, max_percentile: float = 99.0, bit_depth: int = 8) -> None:
        """
        Initialize ContrastStretcher with parameters.
        
        Args:
            min_percentile: Lower percentile for clipping (default 1.0)
            max_percentile: Upper percentile for clipping (default 99.0)
            bit_depth: Bit depth of the image (default 8)
            
        Raises:
            ValueError: If percentiles are invalid or bit_depth is not positive
        """
        if not 0 <= min_percentile <= 100:
            raise ValueError("Min percentile must be between 0 and 100")
        if not 0 <= max_percentile <= 100:
            raise ValueError("Max percentile must be between 0 and 100")
        if min_percentile >= max_percentile:
            raise ValueError("Min percentile must be less than max percentile")
        if bit_depth <= 0:
            raise ValueError("Bit depth must be positive")
            
        self.min_percentile = min_percentile
        self.max_percentile = max_percentile
        self.bit_depth = bit_depth
        self.max_value = (1 << bit_depth) - 1
        self.lut: Optional[List[int]] = None
        self.min_val: Optional[int] = None
        self.max_val: Optional[int] = None
        
    def _build_lut(self, min_val: int, max_val: int) -> List[int]:
        """
        Build lookup table for contrast stretching.
        
        Args:
            min_val: Minimum intensity value after clipping
            max_val: Maximum intensity value after clipping
            
        Returns:
            Lookup table mapping original to stretched values
        """
        if min_val == max_val:
            # Handle edge case where all pixels have the same value
            return [0] * (self.max_value + 1)
            
        lut = []
        scale = self.max_value / (max_val - min_val)
        
        for i in range(self.max_value + 1):
            if i <= min_val:
                lut.append(0)
            elif i >= max_val:
                lut.append(self.max_value)
            else:
                stretched = round((i - min_val) * scale)
                lut.append(min(max(stretched, 0), self.max_value))
                
        return lut
    
    def process_image(self, pixel_data: List[int]) -> List[int]:
        """
        Apply contrast stretching to image pixel data.
        
        Args:
            pixel_data: List of pixel intensity values
            
        Returns:
            List of contrast-stretched pixel values
            
        Raises:
            ValueError: If pixel data is empty
        """
        if not pixel_data:
            raise ValueError("Pixel data cannot be empty")
            
        # Calculate statistics
        stats = ImageStats(pixel_data, self.bit_depth)
        self.min_val = stats.get_percentile(self.min_percentile)
        self.max_val = stats.get_percentile(self.max_percentile)
        
        # Build lookup table
        self.lut = self._build_lut(self.min_val, self.max_val)
        
        # Apply transformation
        result = [self.lut[pixel] for pixel in pixel_data]
        return result
    
    def get_lut(self) -> Optional[List[int]]:
        """
        Get the lookup table if it has been computed.
        
        Returns:
            Lookup table or None if not yet computed
        """
        return self.lut


def _create_test_image(width: int = 64, height: int = 64) -> List[int]:
    """Create a test image with a gradient pattern."""
    pixels = []
    for y in range(height):
        for x in range(width):
            # Create a diagonal gradient from dark to light
            value = int((x + y) * 255 / (width + height - 2))
            pixels.append(min(max(value, 0), 255))
    return pixels


def _print_histogram_stats(stats: ImageStats) -> None:
    """Print histogram statistics."""
    print(f"Total pixels: {stats.total_pixels}")
    print(f"Min value: {min(i for i, v in enumerate(stats.histogram) if v > 0)}")
    print(f"Max value: {max(i for i, v in enumerate(stats.histogram) if v > 0)}")
    
    # Find peaks in histogram
    peak_indices = [i for i, v in enumerate(stats.histogram) if v == max(stats.histogram)]
    print(f"Histogram peak(s) at: {peak_indices}")


def _visualize_image(pixels: List[int], width: int = 64, height: int = 64, title: str = "Image") -> None:
    """Visualize image as ASCII art."""
    print(f"\n{title}:")
    print("-" * (min(width, 40) + 4))
    
    # Sample the image for display if it's too large
    sample_factor = max(1, width // 40)
    display_width = width // sample_factor
    display_height = height // sample_factor
    
    for y in range(0, min(display_height, 20)):  # Limit height for display
        row = ""
        for x in range(display_width):
            idx = (y * sample_factor) * width + (x * sample_factor)
            if idx < len(pixels):
                # Map 0-255 to ASCII characters
                intensity = pixels[idx]
                if intensity < 64:
                    char = " "
                elif intensity < 128:
                    char = "."
                elif intensity < 192:
                    char = "*"
                else:
                    char = "#"
                row += char
            else:
                row += " "
        print(f"|{row}|")
    print("-" * (min(width, 40) + 4))


def main() -> None:
    """Self-test: histogram exact on a planted image, stretch maps a narrow
    band to the full range, monotonicity preserved, degenerate input safe."""
    # Planted image: 100 pixels of value 50, 200 of 100, 100 of 150.
    pixels = [50] * 100 + [100] * 200 + [150] * 100
    stats = ImageStats(pixels)
    assert stats.total_pixels == 400
    assert stats.histogram[50] == 100 and stats.histogram[100] == 200 \
        and stats.histogram[150] == 100, "histogram counts wrong"
    assert sum(stats.histogram) == 400, "histogram must account for every pixel"
    assert stats.histogram[0] == 0 and stats.histogram[255] == 0

    # No-clip stretch of the band [50,150] must use the FULL output range:
    # 50→0, 150→255, and 100 (the midpoint) lands mid-range.
    stretcher = ContrastStretcher(min_percentile=0.0, max_percentile=100.0)
    out = stretcher.process_image(pixels)
    assert stretcher.min_val == 50 and stretcher.max_val == 150, \
        f"detected range wrong: {stretcher.min_val}-{stretcher.max_val}"
    mapped = sorted(set(out))
    assert mapped[0] == 0, f"lowest band value must map to 0, got {mapped[0]}"
    assert mapped[-1] == 255, f"highest band value must map to 255, got {mapped[-1]}"
    assert 120 <= mapped[1] <= 135, f"midpoint must land mid-range, got {mapped[1]}"
    assert len(out) == 400, "stretch changed the pixel count"

    # Monotonic: order of intensities is preserved on a gradient.
    gradient = _create_test_image(64, 64)
    g_out = ContrastStretcher(1.0, 99.0).process_image(gradient)
    by_input = {}
    for src, dst in zip(gradient, g_out):
        by_input.setdefault(src, dst)
    keys = sorted(by_input)
    assert all(by_input[a] <= by_input[b] for a, b in zip(keys, keys[1:])), \
        "contrast stretch broke intensity ordering"
    # Gradient already spans 0..255, so stretching keeps the extremes.
    assert min(g_out) == 0 and max(g_out) == 255

    # Percentile clipping: with 1%-99%, outlier singletons get clipped
    # to the range bounds instead of compressing everyone else.
    with_outliers = [0] + [128] * 998 + [255]
    clip = ContrastStretcher(min_percentile=1.0, max_percentile=99.0)
    c_out = clip.process_image(with_outliers)
    assert clip.min_val == 128 and clip.max_val == 128 or clip.min_val <= 128 <= clip.max_val, \
        f"percentile range should center on the mass: {clip.min_val}-{clip.max_val}"
    assert all(0 <= p <= 255 for p in c_out), "output escaped [0,255]"

    # Degenerate: a flat image must not divide by zero.
    flat_out = ContrastStretcher(0.0, 100.0).process_image([77] * 50)
    assert len(flat_out) == 50
    assert all(0 <= p <= 255 for p in flat_out), "flat image produced out-of-range values"

    print("image_stats: histogram 100/200/100 exact, band [50,150]→[0,255] with "
          "midpoint centered, gradient monotone, flat image safe — PASS")


if __name__ == "__main__":
    main()