import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "L-Moments Flood Frequency Analysis Dashboard",
  description: "Interactive dashboard for L-moments flood frequency analysis results from Terengganu, Malaysia rainfall stations",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="antialiased min-h-screen">
        {children}
      </body>
    </html>
  );
}
