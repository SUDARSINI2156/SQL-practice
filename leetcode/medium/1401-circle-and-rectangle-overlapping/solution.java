class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // Mencari titik terdekat
        int closestX = Math.max(x1, Math.min(xCenter, x2));
        int closestY = Math.max(y1, Math.min(yCenter, y2));
        
        // Menghitung selisih jarak
        int distanceX = xCenter - closestX;
        int distanceY = yCenter - closestY;
        
        // Membandingkan kuadrat jarak dengan kuadrat radius
        return (distanceX * distanceX + distanceY * distanceY) <= (radius * radius);
    }
}
