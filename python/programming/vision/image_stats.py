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
            
        target_count = (percentile / 100.0) * self.total_pixels
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
    """Demonstrate the contrast stretcher functionality."""
    print("Histogram-based Image Contrast Stretcher Demo")
    print("=" * 50)
    
    # Create test image
    print("Creating test image...")
    original_pixels = _create_test_image(64, 64)
    
    # Show original image statistics
    print("\nOriginal Image Statistics:")
    original_stats = ImageStats(original_pixels)
    _print_histogram_stats(original_stats)
    
    # Visualize original image
    _visualize_image(original_pixels, 64, 64, "Original Image")
    
    # Apply contrast stretching
    print("\nApplying contrast stretching (1% - 99% clipping)...")
    stretcher = ContrastStretcher(min_percentile=1.0, max_percentile=99.0)
    stretched_pixels = stretcher.process_image(original_pixels)
    
    # Show results
    print(f"\nContrast stretching applied:")
    print(f"  Original range: {stretcher.min_val} - {stretcher.max_val}")
    print(f"  Stretched to: 0 - {stretcher.max_value}")
    
    # Show stretched image statistics
    print("\nStretched Image Statistics:")
    stretched_stats = ImageStats(stretched_pixels)
    _print_histogram_stats(stretched_stats)
    
    # Visualize stretched image
    _visualize_image(stretched_pixels, 64, 64, "Stretched Image")
    
    # Demonstrate different stretching parameters
    print("\n\nTesting different stretching parameters:")
    test_params = [
        (0.5, 99.5, "Aggressive stretching (0.5%-99.5%)"),
        (5.0, 95.0, "Moderate stretching (5%-95%)"),
        (0.0, 100.0, "No clipping (0%-100%)")
    ]
    
    for min_p, max_p, description in test_params:
        print(f"\n{description}:")
        test_stretcher = ContrastStretcher(min_percentile=min_p, max_percentile=max_p)
        test_pixels = test_stretcher.process_image(original_pixels)
        print(f"  Range mapped from {test_stretcher.min_val}-{test_stretcher.max_val} to 0-{test_stretcher.max_value}")
        _visualize_image(test_pixels, 64, 64, f"Result")


if __name__ == "__main__":
    main()