function Card() {
    return (
        <>
            <div className="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20"
                style={{ height: 80 }}
            >
                <div />
            </div>
            <div className="max-w-xs bg-white shadow-lg rounded-lg overflow-hidden hover:bg-black hover:shadow-xl transition duration-300">
                <img className="w-1/12 max-h-96 object-cover" src="https://www.daytonlocal.com/images/family/techfest.jpg" alt="Card Image" />
                <div className="p-4">
                    <h2 className="text-xl font-bold text-gray-800">Tech-Fest</h2>
                    <p>This is a Tech-fest, especially for tech enthusiasts to participate and win exciting prizes, build connections and explore communities in the tech world</p>
                    <p className="py-2">
                        <i className="fas fa-calendar-check" />
                        <u className="px-2">Friday</u>
                        <br />
                        <u className="px-4">27th NOV 2024</u>
                    </p>
                    <button className="mt-2 px-2 py-2 font-semibold bg-gray-900 text-white rounded active:bg-gray-400 hover:shadow-lg">EXPLORE & Book</button>
                </div>
            </div>
        </>
    );
}

export default Card;