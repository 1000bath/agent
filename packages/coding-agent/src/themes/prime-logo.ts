/**
 * Pre-rendered block logo used by the interactive UI.
 *
 * Spider replacement for the inherited Prime butterfly mark.
 * Keep the legacy export name for protocol/UI compatibility.
 */

/** ~10 rows × 32 cols. Block-style spider logo. */
export const SPIDER_LOGO = ` ▄▄      ▄▄      ▄▄      ▄▄
  ▀██▄  ▄██▀      ▀██▄  ▄██▀
    ▀████   ▄██▄   ████▀
      ▀██████████████▀
  ▄████  ▄██  ██▄  ████▄
 █████  ███ ●● ███  █████
  ▀████  ▀██████▀  ████▀
      ▀████████████▀
    ▄██▀  ▀██  ██▀  ▀██▄
  ▄██▀      ▀██▀      ▀██▄
 ▀▀          ▀▀          ▀▀`;

/** Compact block-style spider logo. */
export const SPIDER_LOGO_COMPACT = ` ▄▄      ▄▄
████████████
 ████  ████
  ▀▀████▀▀`;

/** Backwards-compatible export used by existing interactive UI components. */
export const PRIME_BUTTERFLY_LOGO = SPIDER_LOGO;
