import { useState, useEffect } from 'react';

function UserProfile({ userId }) {

    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        const fetchUser = async () => {

            setLoading(true);

            try {
                const response = await fetch(
                    `https://jsonplaceholder.typicode.com/users/${userId}`
                );

                const data = await response.json();

                setUser(data);

            } catch (error) {
                console.log(error);
            } finally {
                setLoading(false);
            }
        };

        fetchUser();

    }, [userId]);


    if (loading) {
        return <h2>Loading...</h2>;
    }

    return (
        <div>
            <h1>User Profile</h1>

            <p>Name: {user?.name}</p>
            <p>Username: {user?.username}</p>
            <p>Email: {user?.email}</p>
            <p>Phone: {user?.phone}</p>
        </div>
    );
}

export default UserProfile;