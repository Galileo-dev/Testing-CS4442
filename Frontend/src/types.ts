export interface Room {
    id: string;
    name: string;
    capacity: number;
    location: string;
    bookings: Booking[];
}

export interface Booking {
    id: string;
    roomId: string;
    startTime: Date;
    endTime: Date;
}