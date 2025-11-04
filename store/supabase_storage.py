from django.core.files.storage import Storage
from supabase import create_client
from django.conf import settings

class SupabaseStorage(Storage):
    def __init__(self, *args, **kwargs):
        self.supabase_url = settings.SUPABASE_URL
        self.api_key = settings.SUPABASE_API_KEY
        self.bucket_name = settings.SUPABASE_BUCKET_NAME

        # Create Supabase client
        self.client = create_client(self.supabase_url, self.api_key)

    def _save(self, name, content):
        """
        Save the file to Supabase Storage.
        """
        bucket = self.client.storage.from_(self.bucket_name)

        # Upload file (just name and file content)
        bucket.upload(name, content.read())

        # Make file public (optional)
        # bucket.update_public(name)

        return name

    def url(self, name):
        """
        Get the public URL for a file stored in Supabase Storage.
        """
        bucket = self.client.storage.from_(self.bucket_name)
        return bucket.get_public_url(name)

    def exists(self, name):
        """
        Check if a file exists in Supabase Storage.
        """
        bucket = self.client.storage.from_(self.bucket_name)
        files = bucket.list()
        return any(file['name'] == name for file in files)
