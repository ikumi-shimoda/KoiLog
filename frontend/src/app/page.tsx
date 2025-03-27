'use client'
import axios from 'axios'
import { useEffect, useState } from 'react'

export default function Home() {
  const [data, setData] = useState<{ name: string }>({ name: '' })
  const [users, setUsers] = useState<
    { id: number; username: string; email: string; created_at: string }[]
  >([])

  const fetchData = async () => {
    const response = await axios.post('http://localhost:8000/api/', {
      name: 'example',
    })
    setData(response.data)
  }

  const fetchUsers = async () => {
    const response = await axios.get('http://localhost:8000/api/users')
    setUsers(response.data.users)
  }

  return (
    <div>
      <button onClick={fetchData}>pythonとAPI連携</button>
      <div>結果:{data.name}</div>
      <button onClick={fetchUsers}>ユーザー取得</button>
      <div>
        {users.map((user) => (
          <div className='mt-2'>
            <p>user.username</p>
            <p>user.email</p>
            <p>user.created_at</p>
          </div>
        ))}
      </div>
    </div>
  )
}
