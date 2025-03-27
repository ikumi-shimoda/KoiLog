import './globals.css'

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html>
      <body className='bg-red-400 max-w-screen-lg mx-auto'>{children}</body>
    </html>
  )
}
