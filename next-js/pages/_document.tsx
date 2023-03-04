import { ColorModeScript } from "@chakra-ui/react";
import NextDocument, { Html, Head, Main, NextScript } from "next/document";
import Script from "next/script";
import theme from "../lib/theme";
import { NEXT_PUBLIC_GA } from "../lib/gtag";

const isProd = process.env.NODE_ENV === "production";
export default class Document extends NextDocument {
  render() {
    return (
      <Html lang="en">
        <Head>
          {/* Google Analytics */}
          {isProd && (
            <>
              <Script
                id="google-analytics-1"
                strategy="lazyOnload"
                src={`https://www.googletagmanager.com/gtag/js?id=${process.env.NEXT_PUBLIC_GA}`}
              />
              <Script id="google-analytics-2" strategy="lazyOnload">
                {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', '${process.env.NEXT_PUBLIC_GA}', {
          page_path: window.location.pathname,
          });
        `}
              </Script>
            </>
          )}
          {/* SEO:
        https://www.youtube.com/watch?v=imsyg1wRa_Y
        https://cheatcode.co/tutorials/how-to-handle-seo-metadata-in-next-js
        https://github.com/garmeeh/next-seo#usage
        https://nextjs.org/learn/seo/introduction-to-seo
        */}
          <meta charSet="utf-8" />
          <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
          />
          <meta
            name="description"
            content="Get Notified when a research study is up for you"
          />
          <title>Open Seat Notifier</title>
          <link
            rel="icon"
            href="https://ucalgary.sona-systems.com/favicon.ico"
          />
        </Head>

        <body>
          <ColorModeScript initialColorMode={theme.config.initialColorMode} />
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
