from bson.objectid import ObjectId

class Note:
    def __init__(self, title, desc, status=0, _id=None):
        self.title = title
        self.desc = desc
        self.status = status
        self.id = _id

    def save(self, collection):
        """Yangi note'ni saqlash"""
        note_data = {
            "title": self.title,
            "desc": self.desc,
            "status": self.status
        }
        result = collection.insert_one(note_data)
        self.id = result.inserted_id

    @classmethod
    def get_all(cls, collection):
        """Statusi 0 bo'lgan barcha note'larni olish"""
        notes = collection.find({"status": 0})
        return [cls(note['title'], note['desc'], note['status'], str(note['_id'])) for note in notes]

    @classmethod
    def update(cls, collection, note_id, title, desc):
        """Note'ni yangilash"""
        collection.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"title": title, "desc": desc}}
        )

    @classmethod
    def delete(cls, collection, note_id):
        """Note'ni o'chirish (status = -1)"""
        collection.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"status": -1}}
        )
