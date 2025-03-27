'use client'
import axios from 'axios'
import { useEffect, useState } from 'react'

export default function Home() {
  const [data, setData] = useState<{ name: string }>({ name: '' })

  const fetchData = async () => {
    const response = await axios.post('http://localhost:8000/api/', {
      name: 'example',
    })
    setData(response.data)
  }

  return (
    <div>
      <button onClick={fetchData}>pythonとAPI連携</button>
      <div>結果:{data.name}</div>
    </div>
  )
}
