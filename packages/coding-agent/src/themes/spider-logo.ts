/**
 * Pre-rendered ASCII versions of the spider mark.
 *
 * Source: assets/brand/spider.svg
 */

/** ~10 rows × 32 cols. The default brand mark — half-block spider. */
export const SPIDER_LOGO = `        /\     /\\
       {  `---'  }
       {  O   O  }
       ~~>  V  <~~
        \  \|/  /
         `-----'__
         /     \  `^\\_
        {       }\\ |\\_\\_   W
        |  \\_/  |/ /  \\_\\_\\( )
         \\__/  /(_E     \\__/
           (  /
            MM`;

/** Compact spider logo for smaller displays */
export const SPIDER_LOGO_COMPACT = `  /\  /\\
 (OO)(OO)
  \\  ||  /
   \`--'`;

// Backwards compatibility
export const SPIDER_LOGO = SPIDER_LOGO;
