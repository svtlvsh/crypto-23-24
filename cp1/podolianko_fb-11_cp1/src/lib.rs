use std::collections::{HashMap, HashSet};

pub const VALID_LETTERS: &str = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя";

/// Calculate entropy on `probabilities` (log2)
pub fn entropy_from_probabilities<'a, I: Iterator<Item=&'a f64>>(probabilities: I) -> f64 {
    -(probabilities.map(|p| {
        (*p) * (*p).log2()
    }).sum::<f64>())
}

/// returns lowercase string consisting only of `alphabet` characters, or also single whitespaces between words, if `preserve_whitespace` is true.
pub fn normalize_string(string: &str, alphabet: &str, preserve_whitespace: bool) -> String {
    let mut lower_string: String = string.to_lowercase();

    if preserve_whitespace {
        let mut in_whitespace = false;

        // replace all non-alphabet chars with whitespaces
        lower_string = lower_string.replace(|c| {
            !alphabet.contains(c)
        }, " ");

        // preserve only one whitespace between letters
        lower_string.retain(|c| {
            let result: bool = !(c == ' ' && in_whitespace);
            in_whitespace = c == ' ';
            result
        })
    } else {
        lower_string.retain(|c| {
            alphabet.contains(c)
        })
    }

    lower_string
}

/// Calculates frequencies for ngrams in the supplied `text`
/// * `text` - a String of text
/// * `n` - ngram length in characters
/// * `overlap` - will calculate frequencies of overlapping ngrams if true, e.g. 'abcd' wil result in ab=1/3, bc=1/3, cd=1/3;
/// otherwise will count only non-overlapping ngrams, e.g. 'abcd' will result in ab=1/2, cd=1/2
pub fn ngram_frequencies
(
    text: &str,
    n: usize,
    overlap: bool,
)
    -> Result<HashMap<String, f64>, Box<dyn std::error::Error>>
{
    // A vector will suit us well for working with ngrams
    let char_vec: Vec<char> = text.chars().collect();
    let mut count_map: HashMap<String, usize> = HashMap::with_capacity(char_vec.len() + 1 - n);

    for i in (0..char_vec.len() + 1 - n).step_by(if overlap { 1 } else { n }) {
        let ngram: String = char_vec[i..i + n].iter().collect();
        let ngram_count = count_map.entry(ngram).or_insert(0);
        *ngram_count += 1;
    }

    let total: usize = count_map.values().sum();
    let mut frequency_map: HashMap<String, f64> = HashMap::with_capacity(char_vec.len() + 1 - n);

    for (ngram, count) in count_map.drain() {
        frequency_map.insert(ngram, count as f64 / total as f64);
    }

    Ok(frequency_map)
}

pub fn print_freq_table(freq_map: &HashMap<String, f64>) {
    let first_char_set: HashSet<char> = freq_map.keys().into_iter().map(|c| { c.chars().next().expect("must've had one char at least") }).collect();
    let second_char_set: HashSet<char> = freq_map.keys().into_iter().map(|c| { c.chars().skip(1).next().expect("must've had two chars at least") }).collect();
    let mut first_chars_sorted: Vec<char> = first_char_set.into_iter().collect();
    let mut second_chars_sorted: Vec<char> = second_char_set.into_iter().collect();
    first_chars_sorted.sort();
    second_chars_sorted.sort();
    let (table_x, table_y) = (second_chars_sorted.len(), first_chars_sorted.len());


    let float_precision = 4;
    let cell_width = float_precision + 2;

    // print header
    print!("|{:cell_width$}", " ");
    for x in 0..table_x {
        print!("|{:^cell_width$}", second_chars_sorted[x]);
    }
    println!("|");

    // print separator
    print!("|{:-<cell_width$}", "-");
    for x in 0..table_x {
        print!("+{:-<cell_width$}", "");
    }
    println!("|");

    // print rows
    for y in 0..table_y {
        print!("|{:^cell_width$}", first_chars_sorted[y]);
        for x in 0..table_x {
            let key: String = [first_chars_sorted[y], second_chars_sorted[x]].iter().collect();
            print!("|{:^.float_precision$}", freq_map.get(&key).unwrap_or(&0f64));
        }
        println!("|");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn str_normalization_test() {
        let text = "Какой-то \r\n текст";
        assert_eq!(normalize_string(&text, VALID_LETTERS, false), "какойтотекст")
    }

    #[test]
    fn str_normalization_preserve_test() {
        let text = "Какой-то \r\n текст";
        assert_eq!(normalize_string(&text, VALID_LETTERS, true), "какой то текст")
    }
}
