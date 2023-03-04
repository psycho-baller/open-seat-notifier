export const NEXT_PUBLIC_GA = "G-N0EWPN9FF4"

// https://developers.google.com/analytics/devguides/collection/gtagjs/pages
export const pageview = (url: URL): void => {
    // @ts-ignore
    window.gtag("config", NEXT_PUBLIC_GA, {
        page_path: url,
    });
};

type GTagEvent = {
    action: string;
    category: string;
    label: string;
    value: number;
};

// https://developers.google.com/analytics/devguides/collection/gtagjs/events
export const event = ({ action, category, label, value }: GTagEvent): void => {
    window.gtag("event", action, {
        event_category: category,
        event_label: label,
        value,
    });
};