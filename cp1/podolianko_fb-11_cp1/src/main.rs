use std::env;
use std::fs::File;
use std::io::{BufReader, Read, Seek};

use podolianko_fb_11_cp1::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: pass text file location as the ony argument");
        std::process::exit(1);
    }

    let input_file = &args[1];

    println!("Current dir: {}",
             env::current_dir()?
                 .to_str()
                 .unwrap_or("Unknown"));
    println!("Sample file: {input_file}");

    println!();

    let mut with_whitespace = String::new();
    let mut without_whitespace = String::new();
    let mut reader = BufReader::new(File::open(input_file)?);
    reader.read_to_string(&mut with_whitespace)?;
    reader.rewind()?;
    reader.read_to_string(&mut without_whitespace)?;

    // read to String and error on invalid Unicode
    with_whitespace = normalize_string(&with_whitespace, VALID_LETTERS, true);
    without_whitespace = normalize_string(&without_whitespace, VALID_LETTERS, false);

    // Letter frequency calculations

    // With whitespaces
    let pmap = ngram_frequencies(&with_whitespace, 1, false)?;
    let entropy = entropy_from_probabilities(pmap.values());

    println!("Letter frequencies with whitespaces:\n");
    print_freq_plain(&pmap, 5, 4);
    println!("Entropy: {entropy}", entropy = entropy);
    println!("Redundancy: {}", redundancy(entropy, ((VALID_LETTERS.chars().count() as f64 + 1f64) as f64 ).log2()));
    println!();

    // Without whitespaces
    let pmap = ngram_frequencies(&without_whitespace, 1, false)?;
    let entropy = entropy_from_probabilities(pmap.values());

    println!("Letter frequencies without whitespaces:\n");
    print_freq_plain(&pmap, 5, 4);
    println!("Entropy: {entropy}", entropy = entropy);
    println!("Redundancy: {}", redundancy(entropy, (VALID_LETTERS.chars().count() as f64 ).log2()));
    println!();

    // Bigram frequency calculations

    // Overlapping, whitespaces
    let pmap = ngram_frequencies(&with_whitespace, 2, true)?;
    let entropy = entropy_from_probabilities(pmap.values());

    println!("Bigram frequencies overlapping, with whitespace:\n");
    print_bigram_freq_table(&pmap);
    let entropy_per_char = entropy / 2f64;
    println!("Entropy per character: {}", entropy_per_char);
    println!("Redundancy: {}", redundancy(entropy_per_char, ((VALID_LETTERS.chars().count() as f64 + 1f64) as f64 ).log2()));
    println!();

    // Overlapping, without whitespaces
    let pmap = ngram_frequencies(&without_whitespace, 2, true)?;
    let entropy = entropy_from_probabilities(pmap.values());

    println!("Bigram frequencies overlapping, without whitespace:\n");
    print_bigram_freq_table(&pmap);
    let entropy_per_char = entropy / 2f64;
    println!("Entropy per character: {}", entropy_per_char);
    println!("Redundancy: {}", redundancy(entropy_per_char, (VALID_LETTERS.chars().count() as f64 as f64 ).log2()));
    println!();

    // Non-overlapping, whitespaces
    let pmap = ngram_frequencies(&with_whitespace, 2, false)?;
    let entropy = entropy_from_probabilities(pmap.values());

    println!("Bigram frequencies non-overlapping, with whitespace:\n");
    print_bigram_freq_table(&pmap);
    let entropy_per_char = entropy / 2f64;
    println!("Entropy per character: {}", entropy_per_char);
    println!("Redundancy: {}", redundancy(entropy_per_char, ((VALID_LETTERS.chars().count() as f64 + 1f64) as f64 ).log2()));
    println!();

    // Non-overlapping, without whitespaces
    let pmap = ngram_frequencies(&without_whitespace, 2, false)?;
    let entropy = entropy_from_probabilities(pmap.values());

    println!("Bigram frequencies non-overlapping, without whitespace:\n");
    print_bigram_freq_table(&pmap);
    let entropy_per_char = entropy / 2f64;
    println!("Entropy per character: {}", entropy_per_char);
    println!("Redundancy: {}", redundancy(entropy_per_char, (VALID_LETTERS.chars().count() as f64 ).log2()));
    println!();

    //

    Ok(())
}
